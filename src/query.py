from sqlalchemy import text
from sqlalchemy.sql import select, join, func
from sqlalchemy.sql import func
from sqlalchemy.orm import Session


from src.schema import Customer, Order




class Query:
    """
    Creates query object based on
    query.json file. Once the evaluate
    function is called, the q property holds
    the final query.
    """

    q = None
    q_specification = {}

    def __init__(self, q_specification):
        self.q_specification = dict(q_specification)
        self.evaluate()


    def get_table_from_dataset_id(self, id):
        """
        Gets the model like Customer, Order using dataset id.
        """
        for d in self.q_specification["datasets"]:
            if d["id"] == id:
                if d["table"] == "customers":
                    return Customer
                else:
                    return Order


    def select(self, *args):
        """
        function for select operations
        """
        fields = [text(arg) for arg in args]
        self.q = select(*fields)


    def filter(self, *filters):
        """
        function for filter operations
        """
        for f in filters:
            col = f["col"]
            table = self.get_table_from_dataset_id(f["dataset_id"])
            field = getattr(table, col)
            operator = f["operator"]
            params = f.get("param", None)
            if operator == "in":
                self.q = self.q.filter(field.in_(params["value"]))
            if operator == "date_range":
                start_value = params["start_value"]
                end_value = params["end_value"]
                self.q = self.q.filter(field.between(start_value,end_value))

    
    def transform(self, *transformations):
        """
        function for transform operations
        """
        for t in transformations:
            fns = []
            col = t["col"]
            table = self.get_table_from_dataset_id(t["dataset_id"])
            field = getattr(table, col)
            operator = t["operator"]
            params = t.get("param", None)
            if operator=="substring":
                alias = f"{col}_substring"
                fn = func.substr(field, params["start_position"], params["end_position"]).label(alias)
                self.q = select(fn).select_from(self.q)
            if operator=="capitalize":
                alias = f"{col}_capitalize"
                fn = func.upper(field).label(alias)
                self.q = select(fn).select_from(self.q)



            

    def join(self, *joins):
        """
        function for join operations
        """
        for j in joins:
            left = self.get_table_from_dataset_id(j["left"])
            right = self.get_table_from_dataset_id(j["right"])
            left_on = getattr(left, j["left_on"])
            right_on = getattr(right, j["right_on"])
        self.q = self.q.select_from(left)
        self.q = self.q.join(right)



    def evaluate(self):
        if "columns" in self.q_specification:
            self.select(*self.q_specification["columns"])
        else:
            self.select(["*"])

        if "join" in self.q_specification:
            self.join(*self.q_specification["join"])

        if "filter" in self.q_specification:
            self.filter(*self.q_specification["filter"])
        
        if "transformations" in self.q_specification:
            self.transform(*self.q_specification["transformations"])


 
    def execute(self, engine):
        with Session(engine) as session:
            result = session.execute(self.q)
            # for row in result:
            #     print(row)
            return result




 