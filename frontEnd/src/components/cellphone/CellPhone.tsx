import { Icon } from "@iconify/react";
import { MessageContainer } from "../messages/MessageContainer";
import { useEffect, useState } from "react";
import { sendMessage } from "../../services/sendMessages";
import { ContainerTransformText } from "../transformer/ContainerTransformText";

interface CellPhoneProps {
	selectedUser: string | null;
	active: boolean;
	setActive: React.Dispatch<React.SetStateAction<boolean>>;
}

export const CellPhone = ({
	selectedUser,
	active,
	setActive,
}: CellPhoneProps) => {
	const [message, setMessage] = useState("");
	const [newMessage, setNewMessage] = useState("");
	const data = {
		message: message,
		sender: selectedUser,
		receiver: selectedUser === "Austin" ? "John" : "Austin",
	};

	const clickSendMessage = (event: React.ChangeEvent<HTMLInputElement>) => {
		setMessage(event.target.value);
        setNewMessage("");
	};

    const textComplete = () => {
        return newMessage ? `${message} ${newMessage}` : message;
    };
    const sendMessages = async () => {
        try {
            const combinedMessage = textComplete(); 
            await sendMessage({ ...data, message: combinedMessage }); 
            setMessage(""); 
            setNewMessage(""); 
            setActive((prev) => !prev);
        } catch (err) {
            console.log("Error al enviar el mensaje:", err);
        }
    };
    

	return (
		<section className="mx-10">
			<div className="h-[25rem] w-[15rem]">
				<div className="flex justify-center items-center h-6 bg-slate-900 rounded-t-full">
					<div className="bg-white h-2 w-2 rounded-full"> </div>
					<div className="h-2 w-10 bg-white rounded-full ml-2"> </div>
				</div>
				<div className="h-[90%] custom-bg bg-slate-900">
					<div className="h-[79%] p-2 overflow-scroll scroll">
						<MessageContainer active={active} selectedUser={selectedUser} />
					</div>
					<ContainerTransformText
						message={message}
						setNewMessage={setNewMessage}
					/>
					<div className="mx-1 mb-1 flex items-center justify-between">
						<input
							type="text"
							name="text"
							id="text"
							className="rounded-full py-1 px-2 focus:outline-none text-sm font-semibold text-slate-900"
							autoComplete="off"
							aria-label="Type your message"
							value={textComplete()} 
							onChange={clickSendMessage}
						/>
						<Icon
							icon="iconamoon:send-bold"
							className="text-green-300 h-8 w-8 btn-send cursor-pointer"
							aria-label="Send message"
							onClick={sendMessages} 
						/>
					</div>
				</div>

				<div className="flex justify-center items-center h-6 bg-slate-900 rounded-b-full">
					<div className="bg-white h-3 w-6 rounded-full"> </div>
				</div>
			</div>
		</section>
	);
};
