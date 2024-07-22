import React from "react";
import './footerStyle.css';
import Box from "@mui/material/Box";
import Typography from "@mui/material/Typography";
import Toolbar from "@mui/material/Toolbar";
import AppBar from "@mui/material/AppBar";
 
export default function Footer() {
    return (
        <AppBar position="static">
            <Toolbar>
 
                <Typography
                    variant="h6"
                    component="div"
                    sx={{ flexGrow: 1 }}
                >
                    
                </Typography>
            </Toolbar>
        </AppBar>
    );
};

