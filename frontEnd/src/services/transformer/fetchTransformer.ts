const url = "http://127.0.0.1:3000/obtener_salida";

export const fetchMessagesTransformer = async () => {
    try {
        const response = await fetch(url);
        const data = await response.json(); 
        return data;
    } catch (err) {
        console.error("Error en fetch:", err);
        throw err;  
    }
};