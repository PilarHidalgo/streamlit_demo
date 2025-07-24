"""
Data Processor Module

Este módulo proporciona funcionalidades para procesar datos relacionados con información de personas,
específicamente para manipular datos de edad en DataFrames de pandas.

Funciones principales:
    - process_data: Incrementa la edad de todas las personas en el dataset en 1 año.

Ejemplo de uso:
    >>> import pandas as pd
    >>> from data_processor import process_data
    >>> 
    >>> # Crear un DataFrame de ejemplo
    >>> data = pd.DataFrame({
    ...     'name': ['Alice', 'Bob'],
    ...     'age': [25, 30]
    ... })
    >>> 
    >>> # Procesar los datos
    >>> processed_data = process_data(data)
    >>> print(processed_data['age'])
    0    26
    1    31
    Name: age, dtype: int64
"""

import pandas as pd
from typing import Union

def process_data(data: Union[pd.DataFrame, pd.Series]) -> pd.DataFrame:
    """
    Procesa un DataFrame incrementando la edad de cada persona en 1 año.
    
    Esta función toma un DataFrame que contiene información de personas y aumenta
    el valor de la columna 'age' en 1 para cada registro. La función incluye
    validaciones para asegurar la integridad de los datos y evitar modificaciones
    no deseadas en el DataFrame original.

    Args:
        data (Union[pd.DataFrame, pd.Series]): DataFrame o Series de pandas que contiene
            una columna 'age' con valores numéricos representando edades.
        
    Returns:
        pd.DataFrame: Un nuevo DataFrame con las edades incrementadas en 1.
            El DataFrame original no se modifica.
        
    Raises:
        TypeError: Si el input no es un DataFrame o Series de pandas.
        KeyError: Si la columna 'age' no está presente en el DataFrame.
        ValueError: Si los valores en la columna 'age' no son numéricos.
    
    Ejemplo:
        >>> df = pd.DataFrame({'name': ['Alice'], 'age': [25]})
        >>> processed = process_data(df)
        >>> print(processed['age'][0])  # Imprime: 26
    """
    # 1. Validación del tipo de entrada
    # Aseguramos que el input sea un DataFrame o Series de pandas
    if not isinstance(data, (pd.DataFrame, pd.Series)):
        raise TypeError("El input debe ser un DataFrame o Series de pandas")
    
    # 2. Validación de la estructura de datos
    # Verificamos que exista la columna 'age'
    if 'age' not in data.columns:
        raise KeyError("El DataFrame debe contener una columna 'age'")
    
    # 3. Creación de una copia segura
    # Evitamos modificar el DataFrame original creando una copia profunda
    processed_data = data.copy()
    
    # 4. Validación y conversión de tipos de datos
    # Aseguramos que todos los valores en la columna 'age' sean numéricos
    try:
        processed_data['age'] = pd.to_numeric(processed_data['age'])
    except ValueError as e:
        raise ValueError("La columna 'age' debe contener solo valores numéricos") from e
    
    # 5. Procesamiento de datos
    # Incrementamos la edad en 1 año
    processed_data['age'] = processed_data['age'] + 1
    
    return processed_data
