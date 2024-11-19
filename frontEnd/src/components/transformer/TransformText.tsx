

interface TransformTextProps {
	message: string;
	setNewMessage: React.Dispatch<React.SetStateAction<string>>;
}

export const TransformText = ({
	message,
	setNewMessage,
}: TransformTextProps) => {

	const handleClick = () => {
		setNewMessage(message);
	};

	return (
		<>
			<input
				type="button"
				value={message}
				className="min-h-8 max-w-[3.75rem] bg-slate-900 my-1 cursor-pointer text-transformer px-[0.4rem] border-[0.02rem] rounded-xl text-white"
				onClick={handleClick}
			/>
		</>
	);
};
