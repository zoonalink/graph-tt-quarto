"""
Connect to Neo4j DB file.
This file contains connection logic to the Neo4j database.
Author: Petter Lovehagen
"""

import keyring
from neo4j import GraphDatabase
from neo4j.exceptions import AuthError, ServiceUnavailable




def connect_to_neo4j():
    """
    Establishes a connection to the Neo4j database

    Returns:
        driver: A Neo4j driver object used to interact with the database.
    """
    uri = keyring.get_password("neo4j", "uri")
    username = keyring.get_password("neo4j", "username")
    password = keyring.get_password("neo4j", "password")

    print("Connecting to Neo4j database....")

    try:
        driver = GraphDatabase.driver(
            uri,
            auth=(username, password),
            database = 'neo4j'
           
            )
        print(f"Connected to Neo4j database successfully! Driver: {driver}")
        return driver
    except AuthError as e:
        print("Failed to authenticate with Neo4j: %s", e)
        raise  # Re-raise the exception after logging
    except ServiceUnavailable as e:
        print("Neo4j service is unavailable: %s", e)
        raise

