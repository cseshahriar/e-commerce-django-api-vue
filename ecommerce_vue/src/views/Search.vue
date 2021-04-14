<template>
    <div class="page-search">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Search</h1>
                <h2 class="is-size-5 has-text-grey">Search Term: "{{ query }}"</h2>
            </div>

            <ProductBox 
            v-for="product in products"
            v-bind:key="product.id"
            v-bind:product="product"/>
        </div>
    </div>
</template>


<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox'

export default {
    name: 'Search',
    components: {
        ProductBox
    },
    data() {
        return {
            products: [],
            query: ''
        }
    },
    mounted() {
        document.title = 'Search | Ecommerce Store'
        let uri = window.location.search.substring(1)
        let params = new URLSearchParams(uri)

        if (params.get('query')) {
          this.query = params.get('query')
          
          this.performSearch()
        }
    },
    methods: {
        async performSearch() {
            this.$store.commit('setIsLoading', true) // push to vuex

            await axios
                    .post('/api/v1/products/search/', {
                        'query': this.query
                    })
                    .then( response => {
                        this.products = response.data
                    })
                    .catch( error => {
                        console.log(error)
                    })
        }
    }
}
</script>