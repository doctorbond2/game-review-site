export const metadata = {
  title: 'Next.js',
  description: 'Generated by Next.js',
};
import SubmitProvider from '../context/SubmitContext';
import './globals.css';
import Footer from '@/components/nav/footer/Footer';
import Header from '@/components/nav/header/Header';
export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <SubmitProvider>
        <body style={{ paddingTop: '50px', paddingBottom: '100px' }}>
          <Header />

          {children}
          <Footer />
        </body>
      </SubmitProvider>
    </html>
  );
}
