import { Header } from 'components/Header';
import { AppRouter } from './router';
import styles from './App.module.css';
import { BrowserRouter } from 'react-router-dom';

function App() {
  return (
    <div className={styles.app}>
      <Header author='Анкудинов Кирилл' group='P3218'/>
      <main className={styles.main}>
      <BrowserRouter>
        <AppRouter />
      </BrowserRouter>
      </main>
    </div>
  );
}

export default App;