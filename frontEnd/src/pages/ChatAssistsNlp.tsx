import { CellPhone } from "../components/cellphone/CellPhone";
import { User } from "../components/User";
import { MainLayout } from "../layouts/MainLayout";
import Austin from "../assets/Profile/user-3.jpg";
import John from "../assets/Profile/user-1.jpg";
import { useState } from "react";


export const ChatAssistsNlp = () => {

    const [selectedUser, setSelectedUser] = useState<string | null>("Austin");

    const NAME_PROFILE1 = "Austin";
    const NAME_PROFILE2 = "John";

    const [active, setActive] = useState(false);
    const onMessageClick = (name: string) => {
        setSelectedUser(name);
    };


    return (
        <MainLayout>
            <div className="w-full h-full flex justify-center mt-6 items-center">
                <User
                    profile={Austin}
                    name={NAME_PROFILE1}
                    isSelected={selectedUser === NAME_PROFILE1}
                    active={active}
                    onMessageClick={onMessageClick}
                />
                <CellPhone selectedUser={selectedUser} active={active} setActive={setActive}/>
                <User
                    profile={John}
                    name={NAME_PROFILE2}
                    isSelected={selectedUser === NAME_PROFILE2}
                    active={active}
                    onMessageClick={onMessageClick}
                />
            </div>
        </MainLayout>
    );
};
