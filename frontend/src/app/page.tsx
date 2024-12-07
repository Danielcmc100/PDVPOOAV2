import styles from './styles.module.scss'
import HeaderNav from '@/components/HeaderNav';
import LoginForm from '@/components/LoginForm';

export default function Home() {
  return (
    <>
      <HeaderNav />
      <LoginForm />
    </>
  );
}
