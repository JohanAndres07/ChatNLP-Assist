const url = "http://127.0.0.1:3000/procesar_texto";

export const sendMessagesTransformer = async (data:string)=>{
    try{
        await fetch(url,{
            method:'POST',
            headers: {
                'Content-Type': 'application/json',  
            },
            body: JSON.stringify({texto:data}),
        })
    }catch(err){
        console.error("err",err);
    }
}