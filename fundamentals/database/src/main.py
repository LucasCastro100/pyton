from src.operations import CreateTable, AlterTable, DropTable

CreateTable("CREATE TABLE exemplo (id INT PRIMARY KEY)").execute()
# AlterTable("ALTER TABLE exemplo ADD COLUMN nome VARCHAR(255)").execute()
# DropTable("DROP TABLE exemplo").execute()