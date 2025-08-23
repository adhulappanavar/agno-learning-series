"""
Simple SQLite-based Memory Database for Agno
============================================

This is a basic implementation of a memory database that can be used with AgentMemory.
It provides persistent storage for agent memories using SQLite.
"""

import sqlite3
import json
from typing import List, Optional, Dict, Any
from pathlib import Path

class SimpleMemoryDb:
    """
    A simple SQLite-based memory database implementation.
    """
    
    def __init__(self, db_path: str = "memory.db"):
        """
        Initialize the memory database.
        
        Args:
            db_path: Path to the SQLite database file
        """
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize the database tables."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Create memories table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS memories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT,
                    memory_type TEXT,
                    content TEXT,
                    metadata TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create messages table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT,
                    role TEXT,
                    content TEXT,
                    metadata TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            # Create sessions table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sessions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    session_id TEXT UNIQUE,
                    session_name TEXT,
                    summary TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            
            conn.commit()
    
    def create(self, table: str, data: Dict[str, Any]) -> bool:
        """Create a new record in the specified table."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                if table == "memories":
                    cursor.execute("""
                        INSERT INTO memories (user_id, memory_type, content, metadata)
                        VALUES (?, ?, ?, ?)
                    """, (
                        data.get('user_id', 'default'),
                        data.get('memory_type', 'general'),
                        data.get('content', ''),
                        json.dumps(data.get('metadata', {}))
                    ))
                
                elif table == "messages":
                    cursor.execute("""
                        INSERT INTO messages (session_id, role, content, metadata)
                        VALUES (?, ?, ?, ?)
                    """, (
                        data.get('session_id', 'default'),
                        data.get('role', 'user'),
                        data.get('content', ''),
                        json.dumps(data.get('metadata', {}))
                    ))
                
                elif table == "sessions":
                    cursor.execute("""
                        INSERT OR REPLACE INTO sessions (session_id, session_name, summary)
                        VALUES (?, ?, ?)
                    """, (
                        data.get('session_id', 'default'),
                        data.get('session_name', 'default'),
                        data.get('summary', '')
                    ))
                
                conn.commit()
                return True
                
        except Exception as e:
            print(f"Error creating record in {table}: {e}")
            return False
    
    def read_memories(self, user_id: Optional[str] = None, memory_type: Optional[str] = None) -> List[Dict[str, Any]]:
        """Read memories from the database."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                query = "SELECT * FROM memories WHERE 1=1"
                params = []
                
                if user_id:
                    query += " AND user_id = ?"
                    params.append(user_id)
                
                if memory_type:
                    query += " AND memory_type = ?"
                    params.append(memory_type)
                
                query += " ORDER BY created_at DESC"
                
                cursor.execute(query, params)
                rows = cursor.fetchall()
                
                memories = []
                for row in rows:
                    memories.append({
                        'id': row[0],
                        'user_id': row[1],
                        'memory_type': row[2],
                        'content': row[3],
                        'metadata': json.loads(row[4]) if row[4] else {},
                        'created_at': row[5],
                        'updated_at': row[6]
                    })
                
                return memories
                
        except Exception as e:
            print(f"Error reading memories: {e}")
            return []
    
    def upsert_memory(self, user_id: str, memory_type: str, content: str, metadata: Optional[Dict] = None) -> bool:
        """Insert or update a memory."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Check if memory exists
                cursor.execute("""
                    SELECT id FROM memories 
                    WHERE user_id = ? AND memory_type = ? AND content = ?
                """, (user_id, memory_type, content))
                
                existing = cursor.fetchone()
                
                if existing:
                    # Update existing memory
                    cursor.execute("""
                        UPDATE memories 
                        SET metadata = ?, updated_at = CURRENT_TIMESTAMP
                        WHERE id = ?
                    """, (json.dumps(metadata or {}), existing[0]))
                else:
                    # Create new memory
                    cursor.execute("""
                        INSERT INTO memories (user_id, memory_type, content, metadata)
                        VALUES (?, ?, ?, ?)
                    """, (user_id, memory_type, content, json.dumps(metadata or {})))
                
                conn.commit()
                return True
                
        except Exception as e:
            print(f"Error upserting memory: {e}")
            return False
    
    def delete_memory(self, memory_id: int) -> bool:
        """Delete a memory by ID."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM memories WHERE id = ?", (memory_id,))
                conn.commit()
                return True
                
        except Exception as e:
            print(f"Error deleting memory: {e}")
            return False
    
    def clear(self, table: Optional[str] = None) -> bool:
        """Clear all data from specified table or all tables."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                if table:
                    cursor.execute(f"DELETE FROM {table}")
                else:
                    cursor.execute("DELETE FROM memories")
                    cursor.execute("DELETE FROM messages")
                    cursor.execute("DELETE FROM sessions")
                
                conn.commit()
                return True
                
        except Exception as e:
            print(f"Error clearing data: {e}")
            return False
    
    def table_exists(self, table: str) -> bool:
        """Check if a table exists."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT name FROM sqlite_master 
                    WHERE type='table' AND name=?
                """, (table,))
                return cursor.fetchone() is not None
        except Exception:
            return False
    
    def memory_exists(self, user_id: str, memory_type: str, content: str) -> bool:
        """Check if a specific memory exists."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT id FROM memories 
                    WHERE user_id = ? AND memory_type = ? AND content = ?
                """, (user_id, memory_type, content))
                return cursor.fetchone() is not None
        except Exception:
            return False
