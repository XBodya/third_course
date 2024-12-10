package org.example;

import com.opencsv.exceptions.CsvValidationException;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;

import static org.example.MyCSVParser.*;

public class Main {
    public static void main(String[] args) {
        //System.out.println((new File("l4\\src")).getAbsolutePath());
        try {
            ArrayList<Human> res = parseCsv("l4\\src\\main\\resources\\foreign_names.csv");
            for(Human el: res){
                System.out.println(el);
            }
        } catch (IOException | CsvValidationException e) {
            throw new RuntimeException(e);
        }

    }
}

//Tail of out
//Human{id=54165, name='Zulima', gender='Female', subdivide=Subdivision{id=3, name='G'}, salary=9100, birthday=Sun Jun 17 00:00:00 MSK 1951}
//Human{id=54166, name='Zulima', gender='Female', subdivide=Subdivision{id=9, name='D'}, salary=9800, birthday=Wed Aug 13 00:00:00 MSK 1930}
//Human{id=54167, name='Zuri', gender='Female', subdivide=Subdivision{id=5, name='C'}, salary=7300, birthday=Sun Aug 15 00:00:00 MSK 1943}
//Human{id=54168, name='Zuria', gender='Female', subdivide=Subdivision{id=1, name='J'}, salary=2600, birthday=Mon Mar 03 00:00:00 MSK 1930}
//Human{id=54169, name='Zurie', gender='Female', subdivide=Subdivision{id=6, name='O'}, salary=1700, birthday=Sat Apr 23 00:00:00 MSK 1966}
//Human{id=54170, name='Zuriel', gender='Male', subdivide=Subdivision{id=11, name='A'}, salary=6000, birthday=Tue May 25 00:00:00 MSK 1982}
//Human{id=54171, name='Zurina', gender='Female', subdivide=Subdivision{id=10, name='K'}, salary=1100, birthday=Mon Jun 11 00:00:00 MSK 1956}
//Human{id=54172, name='Zurine', gender='Female', subdivide=Subdivision{id=11, name='A'}, salary=5000, birthday=Sat Nov 07 00:00:00 MSK 1936}
//Human{id=54173, name='Zurine', gender='Female', subdivide=Subdivision{id=5, name='C'}, salary=4000, birthday=Fri Oct 16 00:00:00 MSK 1964}
//Human{id=54174, name='Zuwena', gender='Female', subdivide=Subdivision{id=14, name='L'}, salary=3100, birthday=Sun Dec 05 00:00:00 MSK 1943}
//Human{id=54175, name='Zuzana', gender='Female', subdivide=Subdivision{id=1, name='J'}, salary=3900, birthday=Tue Dec 09 00:00:00 MSK 1930}
//Human{id=54176, name='Zwena', gender='Female', subdivide=Subdivision{id=6, name='O'}, salary=7400, birthday=Sat Oct 07 00:00:00 MSK 1995}
//Human{id=54177, name='Zyana', gender='Female', subdivide=Subdivision{id=6, name='O'}, salary=8900, birthday=Sun Jul 08 00:00:00 MSK 1934}
//Human{id=54178, name='Zyta', gender='Female', subdivide=Subdivision{id=4, name='H'}, salary=7600, birthday=Sat Apr 16 00:00:00 MSK 1955}


