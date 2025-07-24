"""
Data Loader Module

Este módulo proporciona funcionalidades robustas para cargar datos desde archivos CSV.
Incluye validaciones, manejo de errores y opciones de configuración flexibles.

Funciones principales:
    - load_data: Carga datos desde archivos CSV con validaciones y manejo de errores
    - validate_file_path: Valida la existencia y formato del archivo

Ejemplo de uso:
    >>> from data_loader import load_data
    >>> 
    >>> # Cargar datos básico
    >>> df = load_data('data/data.csv')
    >>> 
    >>> # Cargar con opciones personalizadas
    >>> df = load_data('data/data.csv', encoding='utf-8', sep=';')
"""

import pandas as pd
import os
import logging
from typing import Optional, Dict, Any
from pathlib import Path

# Configurar logging para el módulo
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_file_path(file_path: str) -> bool:
    """
    Valida si la ruta del archivo es válida y el archivo existe.
    
    Args:
        file_path (str): Ruta al archivo a validar
        
    Returns:
        bool: True si el archivo es válido, False en caso contrario
        
    Raises:
        ValueError: Si la ruta está vacía o es None
        FileNotFoundError: Si el archivo no existe
    """
    # Validar que la ruta no esté vacía
    if not file_path or not isinstance(file_path, str):
        raise ValueError("La ruta del archivo debe ser una cadena no vacía")
    
    # Convertir a Path para mejor manejo
    path = Path(file_path)
    
    # Verificar que el archivo existe
    if not path.exists():
        raise FileNotFoundError(f"El archivo no existe: {file_path}")
    
    # Verificar que es un archivo (no un directorio)
    if not path.is_file():
        raise ValueError(f"La ruta especificada no es un archivo: {file_path}")
    
    # Verificar extensión CSV
    if path.suffix.lower() not in ['.csv', '.txt']:
        logger.warning(f"Advertencia: El archivo no tiene extensión CSV: {file_path}")
    
    return True

def load_data(file_path: str, **kwargs) -> Optional[pd.DataFrame]:
    """
    Carga datos desde un archivo CSV con validaciones y manejo robusto de errores.
    
    Esta función proporciona una interfaz segura para cargar archivos CSV,
    incluyendo validaciones de entrada, manejo de errores y logging detallado.
    
    Args:
        file_path (str): Ruta al archivo CSV a cargar
        **kwargs: Parámetros adicionales para pd.read_csv() como:
            - encoding: Codificación del archivo (default: 'utf-8')
            - sep: Separador de columnas (default: ',')
            - header: Fila de encabezados (default: 0)
            - index_col: Columna a usar como índice
            - na_values: Valores a tratar como NaN
            
    Returns:
        Optional[pd.DataFrame]: DataFrame con los datos cargados, 
                               None si ocurre un error
        
    Raises:
        ValueError: Si los parámetros de entrada son inválidos
        FileNotFoundError: Si el archivo no existe
        pd.errors.EmptyDataError: Si el archivo está vacío
        pd.errors.ParserError: Si hay errores de formato en el CSV
        
    Ejemplo:
        >>> # Uso básico
        >>> df = load_data('data/data.csv')
        >>> 
        >>> # Con parámetros personalizados
        >>> df = load_data('data/data.csv', 
        ...                encoding='latin-1', 
        ...                sep=';',
        ...                na_values=['N/A', 'NULL'])
    """
    try:
        # 1. Validación de la ruta del archivo
        logger.info(f"Iniciando carga de datos desde: {file_path}")
        validate_file_path(file_path)
        
        # 2. Configuración de parámetros por defecto
        default_params = {
            'encoding': 'utf-8',
            'sep': ',',
            'header': 0
        }
        
        # Combinar parámetros por defecto con los proporcionados
        params = {**default_params, **kwargs}
        
        # 3. Carga del archivo CSV
        logger.info(f"Cargando archivo con parámetros: {params}")
        dataframe = pd.read_csv(file_path, **params)
        
        # 4. Validaciones post-carga
        if dataframe.empty:
            logger.warning(f"Advertencia: El archivo está vacío: {file_path}")
            return dataframe
        
        # 5. Información del dataset cargado
        logger.info(f"Datos cargados exitosamente:")
        logger.info(f"  - Filas: {len(dataframe)}")
        logger.info(f"  - Columnas: {len(dataframe.columns)}")
        logger.info(f"  - Columnas: {list(dataframe.columns)}")
        
        return dataframe
        
    except FileNotFoundError as e:
        logger.error(f"Error: Archivo no encontrado - {e}")
        raise
        
    except pd.errors.EmptyDataError as e:
        logger.error(f"Error: El archivo CSV está vacío - {file_path}")
        raise
        
    except pd.errors.ParserError as e:
        logger.error(f"Error: Formato inválido en el archivo CSV - {e}")
        raise
        
    except UnicodeDecodeError as e:
        logger.error(f"Error: Problema de codificación - {e}")
        logger.info("Sugerencia: Intenta con encoding='latin-1' o 'cp1252'")
        raise
        
    except Exception as e:
        logger.error(f"Error inesperado al cargar el archivo: {e}")
        raise

def get_file_info(file_path: str) -> Dict[str, Any]:
    """
    Obtiene información detallada sobre un archivo CSV sin cargarlo completamente.
    
    Args:
        file_path (str): Ruta al archivo CSV
        
    Returns:
        Dict[str, Any]: Diccionario con información del archivo
    """
    try:
        validate_file_path(file_path)
        path = Path(file_path)
        
        # Leer solo las primeras filas para obtener información
        sample_df = pd.read_csv(file_path, nrows=5)
        
        info = {
            'file_name': path.name,
            'file_size_mb': round(path.stat().st_size / (1024 * 1024), 2),
            'columns': list(sample_df.columns),
            'column_count': len(sample_df.columns),
            'data_types': sample_df.dtypes.to_dict(),
            'sample_data': sample_df.head(3).to_dict('records')
        }
        
        return info
        
    except Exception as e:
        logger.error(f"Error obteniendo información del archivo: {e}")
        return {}
