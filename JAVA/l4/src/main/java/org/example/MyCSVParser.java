package org.example;

import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvValidationException;

import java.io.*;
import java.util.ArrayList;

/**
 * Класс для парсинга csv файлов по условиям задачи
 */
public class MyCSVParser {
    /**
     * @param filename имя файла
     * @return лист типа ArrayList с элементами Human, которые были распарсены из файла
     * @throws IOException
     * @throws CsvValidationException
     */
    static public ArrayList parseCsv(String filename) throws IOException, CsvValidationException {
        ArrayList<Human> result = new ArrayList<Human>();
        try {
            FileReader in = new FileReader(filename);
            CSVReader reader = new CSVReader(in);
            String[] nextLine;
            while ((nextLine = reader.readNext()) != null) {
                for (String cell : nextLine) {
                    String[] curData = cell.split(";");
                    if(curData[0].equals("id") || curData.length != 6) continue;
                    result.addLast(new Human(curData));
                }
            }
        } catch (IOException | CsvValidationException e) {
            throw new RuntimeException(e);
        }
        return result;
    }
}
