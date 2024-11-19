const url = "http://127.0.0.1:3000/messages/unread";

export const fetchNotifications = async ()=>{
    try{
        const response = await fetch(url);
        return (await response.json());

    }catch(err){
        console.error("err",err);
    }
}