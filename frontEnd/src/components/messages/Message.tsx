import { useEffect, useState } from "react";

interface MesageProps {
	message: string;
	color: string;
}

export const Message = ({ message, color }: MesageProps) => {
	const [style, setStyle] = useState("");
	const [directionMessage , setDirectionMessage] = useState("");

	useEffect(() => {
		if (color !== "bg-receivedColor" ) {
			setStyle("bg-sendColor rounded-t-xl rounded-s-xl");
			setDirectionMessage("justify-end")
		}else{
			setStyle("bg-receivedColor rounded-e-xl rounded-t-xl");
			setDirectionMessage("justify-start");
		}
	}, [color]);
	return (
		<div className={`flex  mt-2 ${directionMessage}`}>
			<div className={`relative  ${style}  min-h-2 max-w-40 px-2 message text-wrap justify-end`}>
				<p> {message}</p>
			</div>
		</div>
	);
};
