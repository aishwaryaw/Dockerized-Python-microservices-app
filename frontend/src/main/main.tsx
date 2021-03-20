// @ts-ignore
import React, { useState, useEffect } from 'react';
import Wrapper from '../admin/Wrapper';
// @ts-ignore
import {Product} from '../Interfaces/Product';

function Main() {
    const [products, setProducts] = useState([] as Product[])

    useEffect(() => {

        (
            async () =>{
                const response = await fetch('http://localhost:8081/api/products');
                const data = await response.json()
                setProducts(data)
            }
        )();
    
    }, [])

    const likesProduct = async(id)=>{

        const response = await fetch(`http://localhost:8081/api/product/${id}/like`, {
            method : 'POST',
            headers : {'Content-Type':'application/json'}
        });

        // console.log(response);
        if(response.status == 400){
            alert("You can't like the same product again !");
        }
        else{
        setProducts(products.map((product:Product)=>{
            if(product.id == id){
                product.likes = product.likes + 1;
            }
            // console.log(product);
            return product;
        }
        ));
    }
    }

    return (
        <Wrapper>
        <main role='main'>
            <div className="album py-5 bg-light">
                <div className="container">
                    <div className="row">
                        {products && products.map((p:Product)=>{
                            return (
                            <div className="col-md-4" key={p.id}>
                                <div className="card mb-4 shadow-sm">
                                    <img src={p.image} height='100px'/>
                                    <div className='card-body'>
                                    <p className="card-text">{p.title}</p>
                                    <div className="d-flex justify-content-between align-items-center">
                                        <div className="btn-group">
                                            <button type="button" className="btn btn-sm btn-outline-secondary"onClick={() => likesProduct(p.id)}
                                             >
                                                Like
                                            </button>
                                        </div>
                                        <small className="text-muted">{p.likes} likes</small>
                                    </div>

                                </div>
                                </div>
                            </div>
                            )
                        })}
                    </div>
                </div>
            </div>
        </main>
        </Wrapper>
    )
}

export default Main
