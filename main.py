"""
Script principal para generar datos de televisiones.
"""

import argparse
import pandas as pd

from data_generator_app.data_generator import generate_television_data



def main():
    """Función principal del programa."""
    # Configurar el analizador de argumentos
    parser = argparse.ArgumentParser(description='Generador de datos de televisiones')
    parser.add_argument(
        '--rows', 
        type=int, 
        default=1000, 
        help='Número de filas a generar (por defecto: 100)'
    )
    parser.add_argument(
        '--output', 
        type=str, 
        default='television_data.csv', 
        help='Nombre del archivo de salida (por defecto: television_data.csv)'
    )
    parser.add_argument(
        '--format', 
        type=str, 
        choices=['csv', 'json', 'excel'], 
        default='json', 
        help='Formato del archivo de salida (por defecto: csv)'
    )
    
    # Analizar argumentos
    args = parser.parse_args()
    
    # Generar datos
    print(f"Generando {args.rows} registros de datos de televisiones...")
    df = generate_television_data(args.rows)
    
    # Mostrar una muestra de los datos
    print("\nMuestra de los datos generados:")
    print(df.head(5))
    
    # Guardar datos
    if args.format == 'csv':
        output_file = args.output if args.output.endswith('.csv') else f"{args.output}.csv"
        df.to_csv(output_file, index=False)
    elif args.format == 'json':
        output_file = args.output if args.output.endswith('.json') else f"{args.output}.json"
        df.to_json(output_file, orient='records', indent=4)
    elif args.format == 'excel':
        output_file = args.output if args.output.endswith('.xlsx') else f"{args.output}.xlsx"
        df.to_excel(output_file, index=False)
    
    print(f"\nSe han generado exitosamente {args.rows} registros de datos de televisiones y se han guardado en {output_file}")


if __name__ == "__main__":
    main()
