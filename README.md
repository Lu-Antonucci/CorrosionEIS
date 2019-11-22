## Tags utilizados en el archivo "interface.ui"  
\  

### Barra de menú 

- **menu_Archivo**: menú principal, al desplegarlo aparecen las siguientes opciones:
    - **actionAbrir**: le permite al usuario abrir archivos tipo _.csv_.
    - **actionImportar**: opción para importar datos desde archivos _.dat_ (inicialmente generados por potenciostatos de la marca GAMRY).
    - **actionGuardar**: le permite al usuario almacenar los datos en un formato estándar. (Verificar y completar)
    - **actionExit**

### Sección de tabuladores

- **tab_modelo**: título del tabulador para la generación del modelo.
  - **label_cdc**: etiqueta asociada al cuadro de texto para el circuito equivalente. 
  - **plainTextEdit_cdc**: cuadro de texto plano, donde el usuario ingresa el circuito equivalente a ajustar.
  - **label_parámetros**: etiqueta bajo la cual aparecen los parámetros del circuito planteado en plainTextEdit_cdc. 
  - **label_fijar**: etiqueta bajo la cual aparecen los cuadros de selección para fijar los valores de los parámetros durante el ajuste.
  - **label_limiteinferior** y **label_limitesuperior**: etiquetas para los cuadrados de texto plano, en los cuales el usuario informará los valores límites inferiores y superiores, respectivamente, que considere adecuados para el circuito bajo estudio.
  - **label_ajuste**: etiqueta bajo la cual se presentan los valores ajustados por el software.  
\  
- **tab_ajuste**: título del tabulador para la elección del método de ajuste y la ponderación a utilizar.
  - **groupBox_metodo**: contenedor para agrupar elementos tipo check-box relativos al método de ajuste de los datos; las opciones son:
    - **radioButton_levenberg**: si está seleccionada, el ajuste se realiza por el método Levenberg-Marquardt.
    - **radioButton_simplex**: si está seleccionada, el ajuste se realiza por el método Simplex.
  - **groupBox_ponderacion**: contenedor para agrupar elementos tipo check-box relativos a la ponderacion deseada por el usuario para el ajuste de los datos; las opciones son:
    - **radioButton_unitario**: los factores de ponderación son iguales a la unidad.
    - **radioButton_proporcional**: en cada frecuencia, el factor de ponderación es igual a la parte real o imaginaria a dicha frecuencia, según que factor se considere.  
    - **radioButton_moduloZ**: en cada punto, los factores de ponderación son iguales al módulo de impedancia a la frecuencia de ese punto.  
\  
- **tab_simulación**: título del tabulador para la simulación de espectros en un rango de frecuencia seleccionado por el usuario, utilizando los parámetros ajustados por el software.
  - **groupBox_rangofrecuencias**: contenedor para agrupar elementos relativos al rango de frecuencia deseado por el usuario para la simulación de espectros de impedancia; agrupa los siguientes elementos:
     - **label_freqincial** y **label_freqfinal**: etiquetas para los cuadrados de texto plano, en los cuales el usuario informará los valores inicial y final, respectivamente, que considere adecuados para la simulación del espectro de impedancia para el circuito bajo estudio.
     - **plainTextEdit_freqinicial** y **plainTextEdit_freqifinal**: cuadros de texto plano, donde el usuario ingresa los valores en Hz de las frecuencias inicial y final, respectivamente, que desea utilizar durante la simulación.
     
### Sección de gráficos

- **verticalLayout_bode**: layout reservado, en la parte superior derecha de la pantalla, para la presentación del diagrama de Bode de los datos importados por el usuario.
- **verticalLayout_nyquist**: layout reservado, en la parte inferior derecha de la pantalla, para la presentación del diagrama de Nyquist de los datos importados por el usuario.

\  
\  
  
## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/Lu-Antonucci/CorrosionEIS/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Lu-Antonucci/CorrosionEIS/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
