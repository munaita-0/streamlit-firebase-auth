import React, { ReactNode, useEffect, useState } from "react"
import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,
} from "streamlit-component-lib"
import { signInWithPopup, GoogleAuthProvider, signInWithEmailAndPassword } from 'firebase/auth';
import { Button, TextField, Box, Typography, Paper } from '@mui/material';
import { initializeApp, getApps } from 'firebase/app';
import { getAuth, Auth as FirebaseAuth, createUserWithEmailAndPassword } from 'firebase/auth';
import GoogleIcon from '@mui/icons-material/Google';
import EmailIcon from '@mui/icons-material/Email';

interface Props {
  lang: "en" | "jp";
  auth: FirebaseAuth;
}

const translations = {
  en: {
    title: "Login",
    logout: "Logout",
    google: "Login with Google",
    email: "Login with Email",
    emailLabel: "Email Address",
    passwordLabel: "Password",
  },
  jp: {
    title: "ログイン",
    logout: "ログアウト",
    google: "Googleでログイン",
    email: "メールでログイン",
    emailLabel: "メールアドレス",
    passwordLabel: "パスワード",
  }
};

const LoginFormFunction: React.FC<Props> = ({ lang, auth }) => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  useEffect(() => {
    Streamlit.setFrameHeight();
  }, []);

  const handleGoogleLogin = async () => {
    const provider = new GoogleAuthProvider();
    signInWithPopup(auth, provider)
    .then((result) => {
      Streamlit.setComponentValue({ success: true, message: null})
    }).catch((error) => {
      Streamlit.setComponentValue({ success: false, message: error.message})
    });
  };

  const handleEmailLogin = async () => {
    try {
      await signInWithEmailAndPassword(auth, email, password);
      Streamlit.setComponentValue({ success: true });
    } catch (error) {
      const errorMessage = (error as Error).message;
      Streamlit.setComponentValue({ success: false, message: errorMessage });
    }
  };

  return (
    <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', minHeight: '100vh', backgroundColor: '#f5f5f5', padding: 2 }}>
      <Paper elevation={3} sx={{ padding: 4, borderRadius: 2, maxWidth: 400, width: '100%', margin: 2 }}>
        <Typography variant="h4" mb={2} align="center">{translations[lang].title}</Typography>
        <Button
          variant="contained"
          color="primary"
          onClick={handleGoogleLogin}
          startIcon={<GoogleIcon />}
          sx={{ mb: 2, fontSize: '1.2rem', padding: '10px 20px' }}
        >
          {translations[lang].google}
        </Button>
        <Box sx={{ width: '100%', mt: 2 }}>
          <TextField label={translations[lang].emailLabel} value={email} onChange={(e) => setEmail(e.target.value)} fullWidth sx={{ mb: 2 }} />
          <TextField label={translations[lang].passwordLabel} type="password" value={password} onChange={(e) => setPassword(e.target.value)} fullWidth sx={{ mb: 2 }} />
          <Button
            variant="contained"
            color="success"
            onClick={handleEmailLogin}
            startIcon={<EmailIcon />}
            fullWidth
            sx={{ fontSize: '1.2rem', padding: '10px 20px' }}
          >
            {translations[lang].email}
          </Button>
        </Box>
      </Paper>
    </Box>
  )
}

const LogoutFormFunction: React.FC<Props> = ({ lang, auth }) => {
  useEffect(() => {
    Streamlit.setFrameHeight();
  }, []);

  const signOut = () => {
    auth.signOut().then(() => {
      Streamlit.setComponentValue({ success: true });
    }).catch((error) => {
      Streamlit.setComponentValue({ success: false, message: error.message });
    });
  };

  return (
    <Button variant="contained" color="primary" onClick={signOut} >
      {translations[lang].logout}
    </Button>
  )
}

const CheckSessionFunction: React.FC<Props> = ({ lang, auth }) => {
  auth.onAuthStateChanged((user) => {
    if (user) {
      Streamlit.setComponentValue(user.toJSON());
    } else {
      Streamlit.setComponentValue(null);
    }
  });  

  return (<></>)
}

class Auth extends React.Component<ComponentProps> {
  private authInstance;

  constructor(props: ComponentProps) {
    super(props)
    const firebase_config = this.props.args["firebase_config"];
    if (!getApps().length) {
      initializeApp(firebase_config);
    }
    this.authInstance = getAuth();
  }

  public render = (): ReactNode => {
    const name = this.props.args["name"];
    const lang: "en" | "jp" = this.props.args["lang"] === "jp" ? "jp" : "en";

    if (name === "LoginForm") {
      return <LoginFormFunction lang={lang} auth={this.authInstance} />;
    } else if (name === "LogoutForm") {
      return <LogoutFormFunction lang={lang} auth={this.authInstance} />;
    } else if (name === "CheckSession") {
      return <CheckSessionFunction lang={lang} auth={this.authInstance} />;
    } else {
      return <div>Invalid name: {name}</div>
    }
  }
}

export default withStreamlitConnection(Auth);
