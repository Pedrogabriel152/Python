from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"O CPF é inválido"})
        
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':"Não inclua número neste campo"})
        
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':"O campo deve ter 9 digitos"})
        
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':"O formato está incorreto. ex: 11 91234-1234 "})
        
        return data
    
   