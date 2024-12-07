import React from "react";
import styles from "./styles.module.scss"

function LoginForm() {
    return (
        <div className={`${styles.main} row`}>
            <div className="col d-flex justify-content-center align-item-center flex-column">
                <div>
                    <h6 className="text-center">Para Acessar o sistema, Faça seu login</h6>
                <form className={`${styles.tform} m-5`}>
                    <div className="mb-3">
                        <label className="form-label">Email address</label>
                        <input type="email" className="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" />
                            <div id="emailHelp" className="d-none form-text"></div>
                    </div>
                    <div className="mb-3">
                        <label htmlFor="exampleInputPassword1" className="form-label">Password</label>
                        <input type="password" className="form-control" id="exampleInputPassword1" />
                    </div>
                    
                    <button type="submit" className="btn w-100 mt-2">Submit</button>
                </form>
                </div>
            </div>
        </div>
    );
}

export default LoginForm;
