from flask import Flask, Response

app = Flask(__name__)

# Функция для генерации OData метаданных в формате XML
def generate_metadata():
    metadata = '''<?xml version="1.0" encoding="utf-8"?>
<edmx:Edmx Version="4.0" xmlns:edmx="http://docs.oasis-open.org/odata/ns/edmx">
  <edmx:DataServices>
    <Schema xmlns="http://docs.oasis-open.org/odata/ns/edm" Namespace="MyNamespace">
      <EntityType Name="Product">
        <Key>
          <PropertyRef Name="ID"/>
        </Key>
        <Property Name="ID" Type="Edm.String" Nullable="false"/>
        <Property Name="Name" Type="Edm.String" Nullable="false"/>
        <Property Name="Price" Type="Edm.Decimal" Nullable="false"/>
      </EntityType>
      <EntityContainer Name="Container">
        <EntitySet Name="Products" EntityType="MyNamespace.Product"/>
      </EntityContainer>
    </Schema>
  </edmx:DataServices>
</edmx:Edmx>'''
    return metadata

@app.route('/odata/$metadata', methods=['GET'])
def metadata():
    xml = generate_metadata()
    return Response(xml, mimetype='application/xml')

@app.route('/odata/Products', methods=['GET'])
def products():
    products = [
        {"ID": "1", "Name": "Product1", "Price": 10.0},
        {"ID": "2", "Name": "Product2", "Price": 20.0}
    ]
    return {"value": products}

if __name__ == '__main__':
    app.run(debug=True)
