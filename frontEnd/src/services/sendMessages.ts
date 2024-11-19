const url = 'http://127.0.0.1:3000/messages';

export const sendMessage = async (data: object) => {
    try {
        await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',  
            },
            body: JSON.stringify(data),  
        });
    } catch (err) {
        console.error("Error:", err);
    }
}
