import React, {useState, useEffect } from "react";
import {View, Text, Image, Button, TouchableOpacity, TextInput} from 'react-native';
import Ionicons from '@expo/vector-icons/Ionicons';

const Greeting = ({name}) => {
  return (
    <View style = {{alignItems: 'center'}}>
      <Text style = {{fontSize : 26}}>Seja bem vindo, {name}!</Text>
    </View>
  )
} 

export default function LotsOfGreetings() {
  const [count, setCount]= useState(0);
  const [msg, setMsg] = useState('');

  let img = 'https://avatars.githubusercontent.com/u/206371605?v=4'

  function curtir(){
    setCount(count+1)
  }

  useEffect(()=> {
    setMsg('O componente foi alterado '+ count + ' vez(es)')
  },[count])

  return (
    <View style = {{alignItems: 'center', top : 100}}>
      <Greeting name = "Pedro"/>
      <Image source={{ uri: img }} style={{width: 200, height: 200, top: 50}}/>
      <Button onPress={() => curtir()} title='Curtir'/>

      <View style={{display: 'flex', flexDirection:'row', alignItems:'center', top:20}}>          
        <Ionicons name='heart' size={28} color='red' />
        <Text style={{paddingHorizontal:5, fontSize:16}}>{count} curtidas</Text>
      </View>

      <TouchableOpacity onPress={() => setCount(0)} style= {{ width: 100, padding: 10, top:50, backgroundColor: 'green', borderRadius: 8}}>
        <Text style={{ color: '#fff', textAlign: 'center',fontSize: 18 }}>Reset</Text>
      </TouchableOpacity>

      <TextInput keyboardType="email-address" placeholder='Digite aqui...' style={{top: 80}}/>
      <Text style={{ top: 100, fontSize: 14}}>
        {msg}
      </Text>
    </View>
  )
}