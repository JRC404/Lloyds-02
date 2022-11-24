import java.util.ArrayList; // without this, ArrayList will not work

public class App {
    public static void main(String[] args) {

        ArrayList<String> favouriteArtists = new ArrayList<String>();
        ArrayList<Integer> favouriteNumbers = new ArrayList<Integer>();

        favouriteNumbers.add(12);
        favouriteNumbers.add(120);
        favouriteNumbers.add(1200);

        // favouriteNumbers.remove(12); // this will attempt to remove index 12
        favouriteNumbers.remove((Integer) 12); // this will remove the value 12
        favouriteNumbers.remove(Integer.valueOf(1200)); // this will also remove a value... but the one above is preferred
        System.out.println(favouriteNumbers); 

        // Add items
        favouriteArtists.add("Miley Cyrus");
        favouriteArtists.add("Lady Gaga");
        favouriteArtists.add("James Blunt");
        
        System.out.println(favouriteArtists);
        
        // Change items
        favouriteArtists.set(2, "Jimmy Blunt");
        
        try {
            favouriteArtists.set(4, "Queen");
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
        
        System.out.println(favouriteArtists);
        
        System.out.println("This is an essential message.");
        
        // remove items
        favouriteArtists.remove(0); // removeAt(0);
        favouriteArtists.remove("Lady Gaga"); // remove("Lady Gaga");
        favouriteArtists.remove("Lady Gaga"); // Lady doesn't exist but it won't kick up a fuss... it'll just move on.
        
        System.out.println("------");
        System.out.println(favouriteArtists); // Miley, Lady, Jimmy?
        // access / read items
        
        System.out.println("---- below this line ----");
        
        String retrievedValue = favouriteArtists.get(0);
        System.out.println(favouriteArtists.get(0));
        // System.out.println(favouriteArtists.get("Jimmy Blunt"))
        
        
        System.out.println(retrievedValue);
        
        System.out.println("---- foreach below this line ----");
        favouriteArtists.add("Lady Gaga");
        // loop through items
        for (String item : favouriteArtists) {
            System.out.println(item);
        }
        
        System.out.println("---- for below this line ----");
        for(int i = 0; i < favouriteArtists.size(); i++)
        {
            System.out.println(favouriteArtists.get(i));
        }
        // get the length of the ArrayList


        
    }
}