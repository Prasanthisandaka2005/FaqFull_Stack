import React, { useState, useEffect } from "react";
import axios from "axios";
import { Container, Typography, Select, MenuItem, Accordion, AccordionSummary, AccordionDetails } from "@mui/material";
import ExpandMoreIcon from "@mui/icons-material/ExpandMore";
import './App.css'

function App() {
  const [faqs, setFaqs] = useState([]);
  const [language, setLanguage] = useState("en");

  useEffect(() => {
    fetchFAQs();
  }, [language]);

  const fetchFAQs = async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:8000/api/faqs/?lang=${language}`);
      setFaqs(response.data);
    } catch (error) {
      console.error("Error fetching FAQs:", error);
    }
  };

  return (
    <Container className="faq">
      <Typography variant="h4" align="center" gutterBottom>
        Frequently Asked Questions
      </Typography>

      <Select
        className="select"
        value={language}
        onChange={(e) => setLanguage(e.target.value)}
      >
        <MenuItem value="en">English</MenuItem>
        <MenuItem value="hi">Hindi</MenuItem>
        <MenuItem value="bn">Bengali</MenuItem>
        <MenuItem value="fr">French</MenuItem>
        <MenuItem value="es">Spanish</MenuItem>
        <MenuItem value="ta">Tamil</MenuItem>
        <MenuItem value="te">Telugu</MenuItem>
      </Select>

      {faqs.length > 0 ? (
        faqs.map((faq, index) => (
          <Accordion key={index} className="list">
            <AccordionSummary expandIcon={<ExpandMoreIcon />}>
              <Typography>{faq.question || "No question available"}</Typography>
            </AccordionSummary>
            <AccordionDetails>
              <Typography>{faq.answer || "No answer available"}</Typography>
            </AccordionDetails>
          </Accordion>
        ))
      ) : (
        <Typography align="center" color="textSecondary">
          ⚠️ No FAQs available in this language.
        </Typography>
      )}
    </Container>
  );
}

export default App;
