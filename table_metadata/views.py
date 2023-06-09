from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from sqlalchemy import create_engine, inspect, text
from typing import List
import json

@api_view(['POST'])
def get_table_metadata(request):
    connection_string = 'sqlite:///C:/Users/patrick szafranko/Downloads/sqlite-tools-win32-x86-3420000/sqlite-tools-win32-x86-3420000/mydatabase.db'
    if not connection_string:
        return Response({'error': 'Connection string is missing'}, status=400)
    try:
        engine = create_engine(connection_string)
        inspector = inspect(engine)

        table_metadata = []

        with engine.connect() as connection:
            for table_name in inspector.get_table_names():
                columns = inspector.get_columns(table_name)
                query = text(f"SELECT COUNT(*) FROM {table_name}")
                print("SQL Query:", query)
                try:
                    result = connection.execute(query)
                    num_rows = int(result.fetchone()[0])
                except Exception as e:
                    print("Error executing query:", query)
                    print("Exception:", str(e))
                    raise Exception(f"Error executing query: {query}. {str(e)}")
                
                schema = inspector.default_schema_name

                # Convert columns to a list of dictionaries
                column_list = []
                for column in columns:
                    column_dict = {
                        'name': column['name'],
                        'type': str(column['type']),  # Convert column type to string
                        'nullable': column['nullable'],
                        # Include any other properties you need
                    }
                    column_list.append(column_dict)

                table_info = {
                    'table_name': table_name,
                    'columns': column_list,
                    'num_rows': num_rows,
                    'schema': schema
                }
                table_metadata.append(table_info)

        response = {
            'status': 'success',
            'data': table_metadata
        }
    except Exception as e:
        response = {
            'status': 'error',
            'message': str(e)
        }

    return JsonResponse(response)
