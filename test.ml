#load "lib.cma";;

open Loop

let _ =
    loopFile "test.uml" (step Eval.stepn show);
    Printf.printf "---END---\n";
    loopFile "test.uml" (step Eval.stepv show);
    Printf.printf "---END---\n";
