import logo from './logo.svg';
import './App.css';
import {Button, Container, Paper, Fab} from '@material-ui/core';
import { Player, Controls } from '@lottiefiles/react-lottie-player';

function App() {
  return (
    <Container maxWidth="sm" style={{backgroundColor:'#ebebeb'}}>
        <h1 style={{color:'#000000'}}>Lottie Application Example</h1>
        <Paper elevation={3}>
        <Player
            autoplay
            loop
            src="https://assets3.lottiefiles.com/packages/lf20_UJNc2t.json"
            style={{ height: '300px', width: '300px' }}
          >
          <Controls visible={true} buttons={['play', 'repeat', 'frame', 'debug']} />
          
        </Player>
        </Paper>
    </Container>
  );
}

export default App;
