import { useCallback, useEffect, useState } from "react";
import { TransformText } from "./TransformText";
import { sendMessagesTransformer } from "../../services/transformer/sendMessagesTransform";
import { fetchMessagesTransformer } from "../../services/transformer/fetchTransformer";

interface ContainerTransformTextProps {
	message: string;
	setNewMessage: React.Dispatch<React.SetStateAction<string>>;
}

export const ContainerTransformText = ({
	message,
	setNewMessage,
}: ContainerTransformTextProps) => {
	const [data, setData] = useState<string[]>([]);

	
	const sendMessageTransformer = useCallback(async (message: string) => {
		try {
			
				await sendMessagesTransformer(message);
			
		} catch (err) {
			console.error("Error al enviar mensaje:", err);
		}
	}, []);

	
	const getMessageTransformer = useCallback(async () => {
		try {
			const response = await fetchMessagesTransformer();
			setData(response.top_3_palabras);
		} catch (err) {
			console.error("Error al obtener mensaje:", err);
		}
	}, []);

	
	useEffect(() => {
		if (message.length > 0) {
			sendMessageTransformer(message); 
			getMessageTransformer(); 
		}
	}, [message, sendMessageTransformer, getMessageTransformer]);

	return (
		<div className="flex items-center justify-center bg-slate-900 h-[2.4rem] gap-1">
			{data.length > 0
				? data.map((element) => (
						<TransformText
							key={element}
							message={element}
							setNewMessage={setNewMessage}
						/>
					))
				:""}
		</div>
	);
};
