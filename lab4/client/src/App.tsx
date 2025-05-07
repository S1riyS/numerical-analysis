import styles from './App.module.css';
import 'bootstrap/dist/css/bootstrap.min.css';

import { Header } from '@common/components';
import AppRouter from '@common/utils/AppRouter';

function App() {
  return (
    <div className={styles.app}>
      <AppRouter>
        <Header author='Анкудинов Кирилл' group='P3218' />
      </AppRouter>
    </div>
  );
}

export default App;