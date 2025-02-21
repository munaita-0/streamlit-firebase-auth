import { createRoot } from 'react-dom/client';
import AuthForm from "./Auth"

const domNode = document.getElementById("root")
if (domNode) {
   const root = createRoot(domNode)
   root.render(<AuthForm />)
  }
