<template>
    <div class="page-checkout">
        <div class="columns is-multiline">

            <div class="column is-12">
                <h1 class="title">Checkout</h1>
            </div>

            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th><Q></Q></th>
                            <th>Total</th>
                        </tr>
                    </thead>
                    
                    <tbody>
                        <tr v-for="item in cart.items" v-bind:key="item.product.id">
                            <td>{{ item.product.name }}</td>
                            <td>{{ item.product.price }}</td>
                            <td>{{ item.quantity }}</td>
                            <td>${{ getItemTotal(item).toFixed(2) }}</td>
                        </tr>
                    </tbody>

                    <tfoot>
                        <tr>
                            <td colspan="2">Total</td>
                            <td>{{ cartTotalLength }}</td>
                            <td>${{ cartTotalPrice.toFixed(2) }}</td>
                        </tr>
                    </tfoot>

                </table>
            </div>


            <div class="column is-12">
                <h2 class="subtitle">Shipping details</h2>
                <p class="has-text-grey mb-4">* All fields are required</p>
               
                <div class="columns is-multiline">
                    
                    <div class="column is-6">
                        <div class="field">
                            <label>First Name*</label>  
                            <div class="control">
                                <input type="text" class="input" v-model="first_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>Last Name*</label>  
                            <div class="control">
                                <input type="text" class="input" v-model="last_name">
                            </div>
                        </div>

                        <div class="field">
                            <label>E-mail*</label>  
                            <div class="control">
                                <input type="text" class="input" v-model="email">
                            </div>
                        </div>

                        <div class="field">
                            <label>Phone*</label>  
                            <div class="control">
                                <input type="text" class="input" v-model="phone">
                            </div>
                        </div>
                    </div>

                    <div class="column is-6">
                        <div class="field">
                            <label>Address*</label>  
                            <div class="control">
                                <textarea class="input" v-model="address"></textarea>
                            </div>
                        </div>
                        <div class="field">
                            <label>Zipcode*</label>  
                            <div class="control">
                                <input class="input" v-model="zipcode">
                            </div>
                        </div>
                        <div class="field">
                            <label>Place*</label>  
                            <div class="control">
                                <input class="input" v-model="place">
                            </div>
                        </div>
                    </div>
                </div>

                <div class="notification is-danger mt-4" v-if="errors.length">
                    <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                </div>
                <hr>
                
                <div id="card-element" class="mb-5"></div>

                <template v-if="cartTotalLength">
                    <hr>
                    <button class="button is-dark" @click="submitForm">Pay with Stripe</button>
                </template>

            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'Checkout',
    data() {
        return { 
            cart: {
                items: []
            },
            stripe: {},
            card: {},
            first_name: '',
            last_name: '',
            email: '',
            phone: '',
            address: '',
            zipcode: '',
            place: '',
            errors: []
        }
    },
    mounted() {
        document.title = 'Checkout | Ecommerce Store'

        this.cart = this.$store.state.cart
    },
    methods: {
        getItemTotal(item) {
            return item.quantity * item.product.price
        },
        submitForm() {
            this.errors = []

            if(this.first_name === '') {
                this.errors.push('The first name field is required')
            }

            if(this.last_name === '') {
                this.errors.push('The last name field is required')
            }

            if(this.email === '') {
                this.errors.push('The email field is required')
            }

            if(this.phone === '') {
                this.errors.push('The phone field is required')
            }

            if(this.phone === '') {
                this.errors.push('The phone field is required')
            }

            if(this.address === '') {
                this.errors.push('The address field is required')
            }

            if(this.zipcode === '') {
                this.errors.push('The zipcode field is required')
            }

            if(this.place === '') {
                this.errors.push('The place field is required')
            }
        }
    },
    computed: {
        cartTotalPrice() {
            return this.cart.items.reduce((acc, currentValue) => {
                return acc += currentValue.product.price * currentValue.quantity
            }, 0)
        },
        cartTotalLength() {
            return this.cart.items.reduce((acc, currentValue) => {
                return acc += currentValue.quantity
            }, 0)
        }
    }
}
</script>