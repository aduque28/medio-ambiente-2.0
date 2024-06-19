def crearTabla(dataFrame, nombreTabla):
    archivoHTML = dataFrame.to_html()
    with open(f"./tables/{nombreTabla}.html", "w") as archivo:
        archivo.write(
            '''
            <html>
            <head>
            <title>{}</title>
            </head>
            <body>
            '''.format(nombreTabla)
        )
        archivo.write(archivoHTML)
        archivo.write(
            '''
            </body>
            </html>
            '''
        )