import { Footer } from "../components/Footer";
import { Header } from "../components/Header";

interface layoutsProps {
	children: React.ReactNode;
}

export const MainLayout: React.FC<layoutsProps> = ({ children }) => {
	return (
		<section className="flex flex-col min-h-screen">
			<Header />
			<main className="flex-grow">{children}</main>
			<Footer />
		</section>
	);
};
