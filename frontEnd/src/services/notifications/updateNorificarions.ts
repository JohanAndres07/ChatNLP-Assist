const url = "http://127.0.0.1:3000/messages/unread";

export const updateNotification = async (data:object)=>{
    try{
        const response = await fetch(url,{
            method:'PATCH',
            headers: {
                'Content-Type': 'application/json',  
            },
            body:JSON.stringify(data)
        });
        return (await response.json());

    }catch(err){
        console.error("err",err);
    }
}