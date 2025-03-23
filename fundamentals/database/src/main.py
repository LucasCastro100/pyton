import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.operations import CreateTable, AlterTable, DropTable

CreateTable("CREATE TABLE teste2 (id INT PRIMARY KEY)").execute()
# AlterTable("ALTER TABLE exemplo ADD COLUMN nome VARCHAR(255)").execute()
# DropTable("DROP TABLE exemplo").execute()