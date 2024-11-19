# ChatNLP-Assist

Este proyecto tiene dos partes: un **Frontend** y un **Backend**. A continuación, se explica cómo instalar y configurar las dependencias necesarias para cada parte.

## Requisitos Previos

- **Python 3.9** o superior. 🐍
- **Node.js** y **npm** (para el frontend). 💻
## Dependencias
- **Backend** (Pyton 3.9, Flask, Torch).
- **Frontend** (Vite, React, Iconify). 

## Backend

El backend utiliza **Flask**, **Flask-CORS**, **torch** y **venv** para la creación de un entorno virtual. 🔙

### Instalación del Backend

1. **Clona el repositorio**:  
   Si aún no has clonado el repositorio, hazlo con el siguiente comando:
   ```bash
   git clone https://github.com/JohanAndres07/ChatNLP-Assist.git
   cd ChatNLP-Assist/backEnd
2. **Crea entorno virtual**:
   ```bash
   python -m venv venv
3. **Iniciar el entorno virtual**:
   En windows
    ```bash
     .\venv\Scritpts\activate
    ```
   En Linux/MacOs
      ```bash
      source venv/bin/activate
      ```
4. **Instalar dependencias**
   Flask
   ```bash
      pip install flask
   ```
   Flask-cors
   ```bash
      pip install flask-cors
   ```
   Torch
   ```bash
      pip install torch
   ```
5. **Iniciar servidor**
   Api
   ```bash
      python app.py
   ```

## Frontend
El frontend se utiliza Vite, React, Iconify
  ### Instalación del Frontend
1. **Cambiar a la carpeta de FrontEnd**
   ```bash
      cd ChatNLP-Assist/frontEnd
   ```
2. **Inatalar dependencias**
   ```bash
      npm install
   ```
3. **Iniciar el frontend**
   ```bash
      npm run dev
   ```

  

   
