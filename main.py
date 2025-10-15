import json
from kestra import Kestra

with open("kestradata.json", "r") as file:
    data = json.load(file)

name = data.get("user_name")

message = f"Hello, {name}. Let's start!"

Kestra.outputs({"generated_message": message})

print(f"Success!")