import React, { useEffect, useState } from "react";
import { styled } from "@mui/material/styles";
import _ from "lodash";
import Markdown from "react-markdown";

import Alert from "@mui/material/Alert";
import AlertTitle from "@mui/material/AlertTitle";
import Autocomplete from "@mui/material/Autocomplete";
import Box from "@mui/material/Box";
import Card from "@mui/material/Card";
import CardContent from "@mui/material/CardContent";
import Divider from "@mui/material/Divider";
import Grid from "@mui/material/Grid";
import TextField from "@mui/material/TextField";
import { Link as MuiLink } from "@mui/material";
import Typography from "@mui/material/Typography";
import Container from "@mui/material/Container";
import Button from "@mui/material/Button";
import SearchInput from "../components/SearchInput";
import SearchResults from "../components/SearchResults";
import SearchProvider from "../components/SearchProvider";
import Link from "../components/Link";
import Api from "../Api";

import { HomeContent } from "../ContentParsing";
import {HomeImageStyle} from "../../content/ContentConfiguration";

const PREFIX = "Home";
const classes = {
  root: `${PREFIX}-root`,
  cta: `${PREFIX}-cta`
};
const Root = styled("div")(({ theme }) => ({
  [`&.${classes.root}`]: {
    display: "flex",
    alignItems: "center",
    backgroundColor: theme.palette.primary.main
  },
  [`& .${classes.cta}`]: {
    borderRadius: theme.shape.radius
  }
}));



export default function Home({
  user,
  pageTitle,
  setPageTitle,
  message,
  examples
}) {

  return (
    <Container maxWidth="xl">
      <Box sx={{ display: "flex" }}>
        <Grid
          container
          direction="row"
          spacing={2}
        >
          <Grid item >
            <Markdown >{HomeContent["full title"]}</Markdown>
          </Grid>
          {!_.isEmpty(message) && <>
            <Grid item xs={5}>
              <Alert severity="info">{message}</Alert>
            </Grid>
          </>
          }

          <Grid item xs={12} >
            <Card>
              <CardContent>
                <Grid container gap="1em" justifyContent={"space-between"}>
                  <Grid item xs={5}>
                    <Typography
                      variant="div"
                      sx={{ fontWeight: "light" }}
                    > <Markdown>{HomeContent.intro}</Markdown>
                    </Typography>
                      {/*}
                    <Link href="/" target="_blank" rel="noopener noreferrer">
                      <Button
                        size="large"
                        sx={{
                          marginTop: "20px",
                          fontWeight: "bold",
                          border: "1px solid grey"
                        }}
                      >
                        Learn More
                      </Button>
                    </Link>{*/}
                  </Grid>
                  <Grid item xs={6} justifyContent={"center"} flexGrow={2} >
                    <Markdown components={{
                      p: ({ node, ...props }) => <div style={HomeImageStyle} className="home-image" {...props} />
                    }}>
                        {HomeContent.image}
                      </Markdown>
                  </Grid>
                </Grid>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={12}>
            {user ? (
              <Card>
                <CardContent>
                  <Grid container>
                    <Grid item xs={6}>
                      <Typography
                        variant="h5"
                        sx={{ fontWeight: "light", paddingBottom: "5%" }}
                      >
                        Variant Search
                      </Typography>
                      <SearchProvider>
                        <SearchInput inputElementId="home-search" variant="standard" sx={{ minWidth: "30vw" }} />
                        <SearchResults sx={{}} />
                      </SearchProvider>
                    </Grid>
                    <Grid
                      item
                      xs={1}
                      container
                      direction="row"
                      justifyContent="center"
                      alignItems="center"
                    >
                      <Divider orientation="vertical" variant="middle" />
                    </Grid>
                    {examples && (
                      <Grid item xs={5}>
                        <Typography
                          variant="h5"
                          sx={{ fontWeight: "light", paddingBottom: "5%" }}
                        >
                          Example
                        </Typography>
                        <Grid container>
                          {examples.snv ? (
                            <>
                              <Grid item xs={2}>
                                <Typography
                                  variant="body1"
                                  sx={{ fontWeight: "bold" }}
                                >
                                  SNV:
                                </Typography>
                              </Grid>
                              <Grid item xs={10}>
                                <Typography variant="body1">
                                  <Link
                                    to={`/variant/${examples.snv.id}`}
                                    color="primary"
                                  >
                                    {examples.snv.var_id}
                                  </Link>
                                </Typography>
                              </Grid>
                            </>
                          ) : (
                            "..."
                          )}
                          {examples.mt ? (
                            <>
                              <Grid item xs={2}>
                                <Typography
                                  variant="body1"
                                  sx={{ fontWeight: "bold" }}
                                >
                                  Mt:
                                </Typography>
                              </Grid>
                              <Grid item xs={10}>
                                <Typography variant="body1">
                                  Mt example
                                </Typography>
                              </Grid>
                            </>
                          ) : null}
                          {examples.sv ? (
                            <>
                              <Grid item xs={2}>
                                <Typography
                                  variant="body1"
                                  sx={{ fontWeight: "bold" }}
                                >
                                  Sv:
                                </Typography>
                              </Grid>
                              <Grid item xs={10}>
                                <Typography variant="body1">
                                  SV example
                                </Typography>
                              </Grid>
                            </>
                          ) : null}
                        </Grid>
                      </Grid>
                    )}
                  </Grid>
                </CardContent>
              </Card>
            ) : null}
          </Grid>
        </Grid>
      </Box>

      <Box
        sx={{
          width: "100%",
          bgcolor: "#0F3057",
          zIndex: 1000,
          marginTop: "30px",
          padding: "20px"
        }}
      >
        <Box
          sx={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            p: 2,
            flexWrap: "wrap",
            gap: "30px"
          }}
        >
            <Markdown components={{
                      p: ({ node, ...props }) => <div style={{width:"250px"}} className="home-image" {...props} />
                    }}>
                        {HomeContent["footer image"]}
                      </Markdown>
                      {/*}
          <Typography variant="h5" component="div" sx={{ color: "white" }}>
            <Link to="/about" color="inherit">
              About
            </Link>
          </Typography>
          <Typography variant="h5" component="div" sx={{ color: "white" }}>
            <Link to="/terms" color="inherit">
              Terms of Use
            </Link>
          </Typography>
          <Typography variant="h5" component="div" sx={{ color: "white" }}>
            <Link to="/contact" color="inherit">
              Contact
            </Link>
          </Typography>{*/}
        </Box>
      </Box>
    </Container>
  );
}
