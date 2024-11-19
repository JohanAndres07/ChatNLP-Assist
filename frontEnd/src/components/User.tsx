import { Icon } from "@iconify/react";
import { fetchNotifications } from "../services/notifications/fetchNotifications";
import { useEffect, useState, useCallback } from "react";
import { updateNotification } from "../services/notifications/updateNorificarions";

interface UserProps {
	profile: string;
	name: string;
	isSelected: boolean;
	active: boolean;
	onMessageClick: (name: string) => void;
}

interface Notification {
	Austin: number;
	John: number;
}

export const User = ({ profile, name, isSelected, active, onMessageClick }: UserProps) => {
	const [notifications, setNotifications] = useState<Notification>({ Austin: 0, John: 0 });

	const notificationCount = notifications[name as keyof Notification] || 0;


	const getNotifications = useCallback(async () => {
		try {
			const response = await fetchNotifications();
			setNotifications(response);
		} catch (err) {
			console.error("Error al obtener notificaciones:", err);
		}
	}, []);

	const updateUserNotifications = useCallback(async () => {
		try {
			console.log(name);
			await updateNotification({ [name]: 0 });
			getNotifications(); 		
		} catch (err) {
			console.error("Error al actualizar notificaciones:", err);
		}
	}, [getNotifications, name]); 

	useEffect(() => {
		
		if (active || !active) {
			getNotifications();
		}

		
		if (notificationCount > 0 && isSelected) {
			updateUserNotifications();
		}
	}, [active, isSelected, notificationCount, getNotifications, updateUserNotifications]);  

	return (
		<section className={`flex flex-col justify-center items-center w-32 h-[20rem] px-4 border-2 rounded-[1.5rem] shadow-xl shadow-gray-400/50 ${isSelected ? "bg-slate-900" : ""}`}>
			<div>
				<img src={profile} alt="User profile" className="h-[4.3rem] w-[4.3rem] object-cover rounded-full" />
			</div>
			<span className="font-bold font-mono mt-2 text-gray-400">{name}</span>
			<br />
			<nav className="flex flex-col justify-around h-[8rem] w-[4rem] rounded-3xl items-center shadow-inner shadow-slate-400">
				<div className="flex flex-col space-y-2">
					<div className="relative btn-focus">
						<p className="absolute left-5 bg-red-600 h-5 w-5 rounded-full flex items-center justify-center text-white font-mono border-2 border-white">{notificationCount}</p>
						<Icon icon="material-symbols:notifications" className={`text-2xl ${isSelected ? "text-yellow-500" : "text-gray-400"} h-10 w-10 cursor-pointer`} />
					</div>

					<Icon
						icon="jam:messages-alt-f"
						className={`text-2xl h-10 w-10 cursor-pointer ${isSelected ? "text-green-300 scale-110" : "text-gray-300 btn-focus"}`}
						onClick={() => {
							onMessageClick(name);
							updateUserNotifications();
						}}
					/>
				</div>
			</nav>
		</section>
	);
};
