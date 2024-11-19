import { messages } from "../../services/fetchMessages";
import { Message } from "./Message";
import { useEffect, useState } from "react";

interface MessageContainerProps {
    active:boolean;
    selectedUser: string | null;

}

interface objectMessage {
    id: number;
    message: string;
    receiver: string;
    sender: string;
    status: string;
}

export const MessageContainer = ({ active, selectedUser }: MessageContainerProps) => {
    const [data, setData] = useState<objectMessage[]>([]);;

    useEffect(() => {
        const fetchMessage = async () => {
            try{
                const response = await messages();
                setData(response);
            }catch(err){
                console.error(err);
            }
        };
        if(active || !active){
            fetchMessage();
            }
    }, [active]); 

    return (
        <section>
            {data.length > 0 ? (
                data.map((element) => (
                    <Message
                        key={element.id} 
                        message={element.message} 
                        color={element.sender === selectedUser ? "bg-sendColor " : "bg-receivedColor"}
                    />
                ))
            ) : (
                ""
            )}
        </section>
    );
};
