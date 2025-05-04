import React from 'react';
import styles from './Header.module.css';

interface HeaderProps {
  author?: string;
  group?: string;
}

export const Header: React.FC<HeaderProps> = ({ author, group }) => {
  return (
    <header className={styles.header}>
      <div className={styles.content}>
        <h1 className={styles.title}>Вычислительная математика</h1>
        {author && <p className={styles.author}>{author} {group}</p>}
      </div>
    </header>
  );
};