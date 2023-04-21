from models.codes import Code
from flask_sqlalchemy import SQLAlchemy

def code_table_test(db):
    #print("Running test: code_table_test")
    test_code_1 = "test_class_code1"
    code_entry = Code(code=test_code_1)
    test_code_2 = "test_class_code2"
    code_entry2 = Code(code=test_code_2)
    db.session.add(code_entry)
    db.session.add(code_entry2)
    db.session.commit()

    codes = Code.query.all()  # Retrieve all code entries from the "Code" table
    code_returns = [code.code for code in codes]  # Return a list of code value
    print("Code table test: ", code_returns)