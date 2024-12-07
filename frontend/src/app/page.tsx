import styles from './styles.module.scss'

export default function Home() {
  return (
    <div className="row">
      <div className="col d-flex justify-content-center align-items-center" 
        style={{
        backgroundColor: "lightblue",
        padding: "20px",
        borderRadius: "5px",
        textAlign: "center",
      }}>
        <div className={styles.myform}>
          testes
        </div>
      </div>
    </div>
  );
}
