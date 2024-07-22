import * as React from "react";
import './headerStyles.css';
import face from './webicon.png';
 
// importing material UI components
import AppBar from "@mui/material/AppBar";
import Toolbar from "@mui/material/Toolbar";
import Typography from "@mui/material/Typography";
 
export default function Header() {
    return (
        <AppBar position="static">
            <Toolbar>
            <img id="faceIco" src={face} className="App-logo" alt="logo" />
 
                <Typography
                    variant="h6"
                    component="div"
                    sx={{ flexGrow: 0.02 }}
                >
                Justin A
                </Typography>

                <Typography
                    variant="h6"
                    component="div"
                    sx={{ flexGrow: 0.88 }}
                >
                Text and Image API test
                </Typography>
            </Toolbar>
        </AppBar>
    );
}
