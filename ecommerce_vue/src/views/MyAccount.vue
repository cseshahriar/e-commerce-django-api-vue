<template>
    <div class="page-my-account">
        <div class="columns is-multiline">

            <div class="column is-12">
                <h1 class="title">My Account</h1>
            </div>

            <div class="column is-12">
                <button class="button is-danger" @click="logout()">Log out</button>
            </div>

            <div class="column is-12">
                <h2 class="subtitle">My orders</h2>
                <!-- order summery component -->
                <OrderSummery
                v-for="order in orders"
                v-bind:key="order.id"
                v-bind:order="order"/>

            </div>
        </div>
    </div>
</template>

<script>
import OrderSummery from '@/components/OrderSummery.vue'
import axios from 'axios'

export default {
    name: 'MyAccount',
    components:{
        OrderSummery
    },
    data() {
        return {
            orders: []
        }
    },
    mounted() {
        document.title = 'My Account | Ecommerce Store'
        this.getMyOrders()
    }
    ,
    methods: {
        logout() {
            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            localStorage.removeItem('username')
            localStorage.removeItem('userid')

            this.$store.commit('removeToken')
            this.$router.push('/')
        },
        async getMyOrders() {
            this.$store.commit('setIsLoading', true)
            
            await axios
                .get('api/v1/orders/list')
                .then(response => {
                    this.orders = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>