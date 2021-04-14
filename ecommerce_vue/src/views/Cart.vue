<template>
    <div class="page-cart">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Cart</h1>
            </div>

            <div class="column is-12 box">
                <table class="table is-fullwidth" v-if="cartTotalLength">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total</th>
                        </tr>
                    </thead>

                    <tbody>
                        <CartItem
                            v-for="item in cart.items"
                            v-bind:key="item.id"
                            v-bind:initialItem="item"
                            v-on:removeFromCart="removeFromCart"/> <!-- listen the method -->
                    </tbody>
                </table>

                <p v-else>You don't have any product in your cart...</p>
            </div>

            <div class="column is-12">
                <h2 class="subtitle">Summery</h2>
                <strong>${{ cartTotalPrice.toFixed(0)}}</strong>, {{ cartTotalLength }} items
                <hr>
                <router-link to="/cart/checkout" class="button is-dark">Proceed to checkout</router-link>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import CartItem from '@/components/CartItem.vue'

export default {
    name: 'Cart',
    components: {
        CartItem
    },
    data() {
        return {
            cart: {
                items: []
            }
        }
    },
    mounted() {
        this.cart = this.$store.state.cart
    },
    methods: {
        removeFromCart(item) {
            this.cart.items = this.cart.items.filter( i => i.product.id !== item.product.id)
        }
    },
    computed: {
        
        cartTotalLength() {
            return this.cart.items.reduce( (acc, currentValue) => {
                return acc += currentValue.quantity
            },0)
        },
        cartTotalPrice() {
            return this.cart.items.reduce((acc, currentValue) => {
                return acc += currentValue.product.price * currentValue.quantity
            }, 0)
        }

    }

}
</script>